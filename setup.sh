mkdir -p `/.streamlit/

echo "\
[server]\n\
port = $PORT\n\n
enableCORS = false\n\
\n\
" > `/.streamlit/config.toml