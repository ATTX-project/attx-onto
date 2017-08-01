if pip freeze | grep -F ontodocs; then
    echo "All is peachy."
else
    pip install docs
fi

python docs_script.py
