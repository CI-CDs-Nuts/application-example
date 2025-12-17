let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +14 ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/main.py
badd +6 ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/compose.yml
badd +5 ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/trigger.py
badd +1 ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/.gitignore
badd +1 ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/.dagger/src/python_dramatiq_example/main.py
badd +34 ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/.github/workflows/push-container.yml
badd +1 dagger.json
argglobal
%argdel
edit ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/compose.yml
argglobal
balt ~/projects/dees_nuts/mono-dees-nuts/apps/python_dramatiq_example/main.py
setlocal foldmethod=manual
setlocal foldexpr=0
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
silent! normal! zE
let &fdl = &fdl
let s:l = 6 - ((5 * winheight(0) + 34) / 68)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 6
normal! 07|
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
let g:this_session = v:this_session
let g:this_obsession = v:this_session
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
