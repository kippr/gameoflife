autocmd BufWritePost *.py exec '!python3 ' shellescape(@%, 1) ' && git commit -m "wip" -a || git reset --hard'
set autoread
