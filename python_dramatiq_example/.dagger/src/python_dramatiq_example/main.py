from typing import Annotated, List

import dagger
from dagger import DefaultPath, dag, function, object_type


@object_type
class PythonDramatiqExample:
    app_directory: Annotated[dagger.Directory, DefaultPath("./")]

    @function
    async def build_container(self) -> dagger.Container:
        return (
            dag.container()
            .from_("ghcr.io/astral-sh/uv:0.8.14-alpine")
            .with_directory("/app", self.app_directory)
            .with_workdir("/app")
            .with_exec(["uv", "sync", "--frozen", "--no-cache", "--no-dev"])
            .with_entrypoint(["uv", "run", "--no-sync"])
        )

    @function
    async def push_container(
        self,
        image_repository: str,
        tags: List[str],
        token: dagger.Secret,
        username: str,
    ) -> dagger.Container:
        """push container to image registry"""
        repo = image_repository.lower()
        container = (await self.build_container()).with_registry_auth(
            repo, username, token
        )

        for tag in tags:
            await container.publish(f"{repo}:{tag}")

        return container

    @function
    def lint(self) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        return (
            dag.container()
            .from_("ghcr.io/astral-sh/uv:0.8.14-debian")
            .with_directory("/app", self.app_directory)
            .with_workdir("/app")
            .with_exec(
                [
                    "/bin/sh",
                    "-c",
                    """
            uv run --with pyright pyright
            """,
                ]
            )
        )

    @function
    def test(self) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        container = (
            dag.container()
            .from_("ghcr.io/astral-sh/uv:0.8.14-debian")
            .with_directory("/app", self.app_directory)
            .with_workdir("/app")
        )

        return (
            dag.testcontainers()
            .setup(container)
            .with_exec(
                [
                    "/bin/sh",
                    "-c",
                    """
            uv run --with pytest pytest
            """,
                ]
            )
        )

    @function
    async def ci(self) -> dagger.Container:
        await self.lint()
        await self.test()
        return await self.build_container()
