
### [Windows offensive security tools](https://wadcoms.github.io/)

### Environment Variables

see all useful variables
```
set
```

see a specific variable
```
set [variable_name]
```

like linux whomai
```
set username
```

shows where .EXEs are
```
set path
```

look for file in directory
```
dir /b /s [directory]\[file]
```

net user

net localgroup

net localgroup administrators

net user [logon_name] [password] /add

net localgroup administrators [logon_name] /add

net user USERNAME /domain

### Domain Groups

net group [GroupName] /domain

net group "Domain Admins" /domain

net group /domain

net group "Domain Admins" username /domain /add

net localgroup [group] [logon_name] /del

net user [logon_name] /del


see config of windows firewall
```
netsh advfirewall show allprofiles
```

### Scraping Files

print file content
```
type [file]
```

look up multiple files
```
type *.txt
type [file1] [file2]
```

display output one page at a time
```
more [file]
```

search for a string within a file
```
type [file] | find /i "[string]"
```

### Registry
Read
```
reg query [KeyName]
```

change a reg key
```
reg add [keyName] /v [ValueName] /t [type] /d [Data]
```

export settings from reg file
```
reg export [KeyName] [filename.reg]
```

import settings from reg file

```
reg import [filename.reg]
```



[^1]: SANS SEC560