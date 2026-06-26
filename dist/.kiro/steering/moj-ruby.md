---
inclusion: fileMatch
fileMatchPattern: '**/*.rb'
description: MoJ Ruby-specific standards
---

# MoJ Ruby Standards

## Ruby – exceptions at application level

Handle exceptions at application level, not in libraries. Exceptions are for unexpected/unhandleable, not flow control.
Always put specific exception types in rescue statements unless there is good reason not to.


## Ruby – meta-programming with caution

Use meta-programming with extreme caution; it makes code harder to read, debug, and can cause performance issues (e.g. method cache purging).

