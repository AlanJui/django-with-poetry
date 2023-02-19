# 《專案指引》

目的：建置「以 Poetry 用於管理 Python 套件」的 Django 專案模版。

參考：
<https://rasulkireev.com/managing-django-with-poetry/>

# Create Project

**(1)**

    ❯ cd ~/workspace/django
    ❯ poetry new ex-2023-02 && cd $_

    ❯ pyenv local 3.10.6
    ❯ pyenv shell
    ❯ python -m venv .venv
    ❯ ls -al
    total 16
    drwxr-xr-x   8 alanjui  staff   256  2 19 14:23 .
    drwxr-xr-x  42 alanjui  staff  1344  2 19 14:19 ..
    -rw-r--r--   1 alanjui  staff     7  2 19 14:22 .python-version
    drwxr-xr-x   6 alanjui  staff   192  2 19 14:23 .venv
    -rw-r--r--   1 alanjui  staff     0  2 19 14:19 README.md
    drwxr-xr-x   3 alanjui  staff    96  2 19 14:19 ex_2023_02
    -rw-r--r--   1 alanjui  staff   308  2 19 14:19 pyproject.toml
    drwxr-xr-x   3 alanjui  staff    96  2 19 14:19 tests

    ❯ poetry env info

    Virtualenv
    Python:         3.10.6
    Implementation: CPython
    Path:           /Users/alanjui/workspace/django/ex-2023-02/.venv
    Executable:     /Users/alanjui/workspace/django/ex-2023-02/.venv/bin/python
    Valid:          True

    System
    Platform:   darwin
    OS:         posix
    Python:     3.10.6
    Path:       /Users/alanjui/.pyenv/versions/3.10.6
    Executable: /Users/alanjui/.pyenv/versions/3.10.6/bin/python3.10

**(2)**

    ❯ poetry shell
    Spawning shell within /Users/alanjui/workspace/django/ex-2023-02/.venv
    ❯ emulate bash -c '. /Users/alanjui/workspace/django/ex-2023-02/.venv/bin/activate'

**(3)**

    ❯ poetry add django
    Using version ^4.1.7 for django

    Updating dependencies
    Resolving dependencies... (0.3s)

    Writing lock file

    Package operations: 3 installs, 0 updates, 0 removals

      • Installing asgiref (3.6.0)
      • Installing sqlparse (0.4.3)
      • Installing django (4.1.7)

    ❯ ls -al .venv/lib/python3.10/site-packages
    total 8
    drwxr-xr-x  15 alanjui  staff   480  2 19 14:30 .
    drwxr-xr-x   3 alanjui  staff    96  2 19 14:23 ..
    drwxr-xr-x  12 alanjui  staff   384  2 19 14:30 Django-4.1.7.dist-info
    drwxr-xr-x   5 alanjui  staff   160  2 19 14:23 _distutils_hack
    drwxr-xr-x  14 alanjui  staff   448  2 19 14:30 asgiref
    drwxr-xr-x   9 alanjui  staff   288  2 19 14:30 asgiref-3.6.0.dist-info
    -rw-r--r--   1 alanjui  staff   151  2 19 14:23 distutils-precedence.pth
    drwxr-xr-x  21 alanjui  staff   672  2 19 14:30 django
    drwxr-xr-x   9 alanjui  staff   288  2 19 14:23 pip
    drwxr-xr-x  10 alanjui  staff   320  2 19 14:23 pip-22.2.1.dist-info
    drwxr-xr-x   6 alanjui  staff   192  2 19 14:23 pkg_resources
    drwxr-xr-x  48 alanjui  staff  1536  2 19 14:23 setuptools
    drwxr-xr-x  10 alanjui  staff   320  2 19 14:23 setuptools-63.2.0.dist-info
    drwxr-xr-x  16 alanjui  staff   512  2 19 14:30 sqlparse
    drwxr-xr-x  11 alanjui  staff   352  2 19 14:30 sqlparse-0.4.3.dist-info

    ❯ cat pyproject.toml
    [tool.poetry]
    name = "ex-2023-02"
    version = "0.1.0"
    description = ""
    authors = ["居正中 <AlanJui.1960@gmail.com>"]
    readme = "README.md"
    packages = [{include = "ex_2023_02"}]

    [tool.poetry.dependencies]
    python = "^3.10"
    django = "^4.1.7"


    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"

**(4)**

    ❯ django-admin startproject web_app .

    ❯ ls -al
    total 32
    drwxr-xr-x  11 alanjui  staff   352  2 19 14:31 .
    drwxr-xr-x  42 alanjui  staff  1344  2 19 14:19 ..
    -rw-r--r--   1 alanjui  staff     7  2 19 14:22 .python-version
    drwxr-xr-x   6 alanjui  staff   192  2 19 14:23 .venv
    -rw-r--r--   1 alanjui  staff     0  2 19 14:19 README.md
    drwxr-xr-x   3 alanjui  staff    96  2 19 14:19 ex_2023_02
    -rwxr-xr-x   1 alanjui  staff   663  2 19 14:31 manage.py
    -rw-r--r--   1 alanjui  staff  2243  2 19 14:30 poetry.lock
    -rw-r--r--   1 alanjui  staff   326  2 19 14:30 pyproject.toml
    drwxr-xr-x   3 alanjui  staff    96  2 19 14:19 tests
    drwxr-xr-x   7 alanjui  staff   224  2 19 14:31 web_app

    ❯ tree .
    .
    ├── README.md
    ├── ex_2023_02
    │   └── __init__.py
    ├── manage.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── tests
    │   └── __init__.py
    └── web_app
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

    4 directories, 11 files

**(5)**

    ❯ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying auth.0010_alter_group_name_max_length... OK
      Applying auth.0011_update_proxy_permissions... OK
      Applying auth.0012_alter_user_first_name_max_length... OK
      Applying sessions.0001_initial... OK

**(6)**

    ❯ python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    February 19, 2023 - 06:39:15
    Django version 4.1.7, using settings 'web_app.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

# Create Django Application

**(1)**

    ❯ python manage.py startapp hello
    ❯ ll
    total 280
    -rw-r--r--  1 alanjui  staff     0B Feb 15 17:13 README.md
    -rw-r--r--  1 alanjui  staff   128K Feb 15 17:22 db.sqlite3
    drwxr-xr-x  3 alanjui  staff    96B Feb 15 17:13 ex_2023_02
    drwxr-xr-x  9 alanjui  staff   288B Feb 15 17:30 hello
    -rwxr-xr-x  1 alanjui  staff   663B Feb 15 17:21 manage.py
    -rw-r--r--  1 alanjui  staff   2.1K Feb 15 17:18 poetry.lock
    -rw-r--r--  1 alanjui  staff   326B Feb 15 17:18 pyproject.toml
    drwxr-xr-x  3 alanjui  staff    96B Feb 15 17:13 tests
    drwxr-xr-x  8 alanjui  staff   256B Feb 15 17:22 web_app

    ❯ tree .
    .
    ├── README.md
    ├── db.sqlite3
    ├── ex_2023_02
    │   └── __init__.py
    ├── hello
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── tests
    │   └── __init__.py
    └── web_app
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-310.pyc
        │   ├── settings.cpython-310.pyc
        │   ├── urls.cpython-310.pyc
        │   └── wsgi.cpython-310.pyc
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

    7 directories, 23 files

**(2) web_app/settings.py**

    ALLOWD_HOSTS = [
      'localhost',
      '127.0.0.1',
    ]
    ...
    INSTALLED_APPS = [
        'hello',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

# Setup Project Configuration

## git

**(1)**

    cp ~/.config/nvim/tools/django/.gitignore .
    git init

## pyright

**(2)**

    ❯ poetry add django-stubs --group dev
    ❯ cp ~/.config/nvim/tools/django/pyrightconfig.json .
    ❯ cp ~/.config/nvim/tools/django/.yabs .

[pyrightconfig.json]

    {
      "venvPath": "./",
      "venv": ".venv",
            "exclude": [
                    "**/node_modules",
                    "**/__pycache__",
                    "**/.venv",
                    "**/.*"
            ],
            "ignore": [
                    "**/node_modules",
                    "**/__pycache__"
            ],
            "reportUnusedVariable": false,
            "reportUnusedFunction": false,
            "reportUnusedImport": true,
            "reportMissingImports": true,
            "reportMissingTypeStubs": "error",
            "reportOptionalMemberAccess": false,
            "reportGeneralTypeIssues": "warning",
            "typeshedPaths": [],
            "typeCheckingMode": "basic",
            "useLibraryCodeForTypes": true
    }

## Verify pyright

    ❯ ~/.local/share/nvim/mason/bin/pyright -p pyrightconfig.json manage.py
    Loading configuration file at /Users/alanjui/workspace/django/ex-2023-02/pyrightconfig.json
    Assuming Python version 3.10
    Assuming Python platform Darwin
    stubPath /Users/alanjui/workspace/django/ex-2023-02/typings is not a valid directory.
    Searching for source files
    Found 1 source file
    pyright 1.1.294
    0 errors, 0 warnings, 0 informations
    Completed in 0.64sec

    ❯ mkdir typings
    ❯ ~/.local/share/nvim/mason/bin/pyright -p pyrightconfig.json manage.py
    Loading configuration file at /Users/alanjui/workspace/django/ex-2023-02/pyrightconfig.json
    Assuming Python version 3.10
    Assuming Python platform Darwin
    Searching for source files
    Found 1 source file
    pyright 1.1.294
    0 errors, 0 warnings, 0 informations
    Completed in 0.636sec


    ❯ pyright -p pyrightconfig.json manage.py
    Loading configuration file at /Users/alanjui/workspace/django/ex-2023-01/pyrightconfig.json
    Config "reportMissingTypeStubs" entry must be true, false, "error", "warning", "information" or "none".
    venvPath /Users/alanjui/workspace/django/ex-2023-01/$HOME/workspace/django/ex-2023-01 is not a valid directory.
    venv .venv subdirectory not found in venv path /Users/alanjui/workspace/django/ex-2023-01/$HOME/workspace/django/ex-2023-01.
    stubPath /Users/alanjui/workspace/django/ex-2023-01/typings is not a valid directory.
    Searching for source files
    Found 1 source file
    pyright 1.1.294
    0 errors, 0 warnings, 0 informations
    Completed in 0.931sec

## yabs

    cp ~/.config/nvim/tools/django/.yabs .

## pylint

    poetry add pylint pylint-django --group dev
    cp ~/.config/nvim/tools/django/.pylintrc .

[.pylintrc]

    [MASTER]
    persistent=yes
    ignore=tests.py, urls.py, migrations
    init-hook="import sys; import os; from pylint.config import find_pylintrc; sys.path.append(os.path.dirname(find_pylintrc()))"
    load-plugins=pylint_django
    django-settings-module=web_app.settings

    [MESSAGES CONTROL]
    # C0111 Missing docstring
    # C0114(missing-module-docstring) Missing module docstring
    # I0011 Warning locally suppressed using disable-msg
    # I0012 Warning locally suppressed using disable-msg
    # W0704 Except doesn't do anything Used when an except clause does nothing but "pass" and there is no "else" clause
    # W0142 Used * or * magic* Used when a function or method is called using *args or **kwargs to dispatch arguments.
    # W0212 Access to a protected member %s of a client class
    # W0232 Class has no __init__ method Used when a class has no __init__ method, neither its parent classes.
    # W0611(unused-import)
    # W0613 Unused argument %r Used when a function or method argument is not used.
    # W0702 No exception's type specified Used when an except clause doesn't specify exceptions type to catch.
    # R1710(inconsistent-return-statements)
    # R0201 Method could be a function
    # C1001 Used when a class is defined that does not inherit from anotherclass and does not inherit explicitly from “object”.
    # C0103 Invalid module name
    # R0901 Used when class has too many parent classes, try to reduce this to get a simpler (and so easier to use) class.
    # E501(flake8): line too long ( > 79 characters )
    # disable=C0111,I0011,I0012,W0704,W0142,W0212,W0232,W0613,W0702,R0201,C1001,C0103,R0901,E501
    disable=raw-checker-failed,
            bad-inline-option,
            locally-disabled,
            file-ignored,
            suppressed-message,
            useless-suppression,
            deprecated-pragma,
            use-symbolic-message-instead,
            too-many-instance-attributes,
            len-as-condition,
            too-few-public-methods,
            anomalous-backslash-in-string,
            no-else-return,
            simplifiable-if-statement,
            too-many-arguments,
            duplicate-code,
            no-name-in-module,
            no-member,
            import-error,
            missing-module-docstring,
            missing-docstring,
            invalid-name,
            consider-using-enumerate


    [REPORTS]
    msg-template={path}:{line}: [{msg_id}({symbol}), {obj}] {msg}


    [BASIC]
    no-docstring-rgx=__.*__|_.*
    class-rgx=\[A-Z_\][a-zA-Z0-9_]+$
    function-rgx=\[a-zA_\][a-zA-Z0-9_]{2,70}$
    method-rgx=\[a-z_\][a-zA-Z0-9_]{2,70}$
    const-rgx=((\[A-Z_\][A-Z0-9_]*)|(\[a-z_\][a-z0-9_]*)|(__.*__)|register|urlpatterns)$
    good-names=_,i,j,k,e,qs,pk,setUp,tearDown

    [TYPECHECK]

    # Tells whether missing members accessed in mixin class should be ignored. A
    # mixin class is detected if its name ends with "mixin" (case insensitive).
    ignore-mixin-members=yes

    # List of classes names for which member attributes should not be checked
    # (useful for classes with attributes dynamically set).
    ignored-classes=SQLObject,WSGIRequest

    # List of members which are set dynamically and missed by pylint inference
    # system, and so shouldn't trigger E0201 when accessed.
    # generated-members=objects,DoesNotExist,id,pk,_meta,base_fields,context
    generated-members=REQUEST,acl_users,aq_parent,objects,_meta,id,[a-zA-Z]+_set

    # List of method names used to declare (i.e. assign) instance attributes
    defining-attr-methods=__init__,__new__,setUp


    [VARIABLES]
    init-import=no
    dummy-variables-rgx=_|dummy

    [SIMILARITIES]
    min-similarity-lines=6
    ignore-comments=yes
    ignore-docstrings=yes


    [MISCELLANEOUS]
    notes=FIXME,XXX,TODO


    [FORMAT]
    max-line-length=120
    max-module-lines=500
    indent-string='    '


    [DESIGN]
    max-args=10
    max-locals=15
    max-returns=6
    max-branches=12
    max-statements=50
    max-parents=13
    max-attributes=7
    min-public-methods=0
    max-public-methods=50

## mypy

    poetry add mypy django-stubs --group dev
    cp ~/.config/nvim/tools/django/mypy.ini

[mypy.ini]

    [mypy]
    plugins =
        mypy_django_plugin.main

    [mypy.plugins.django-stubs]
    django_settings_module = "web_app.settings"

## Django Development Environment

**pyproject.toml**

    [tool.poetry]
    name = "ex-2023-02"
    version = "0.1.0"
    description = ""
    authors = ["居正中 <AlanJui.1960@gmail.com>"]
    readme = "README.md"
    packages = [{include = "ex_2023_02"}]

    [tool.poetry.dependencies]
    python = "^3.10"
    django = "^4.1.7"


    [tool.poetry.group.dev.dependencies]
    django-stubs = "^1.14.0"

    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"

## Neovim

**LSP**

- pyright
- cssls
- emmet_ls
- html-lsp
- json-lsp
- typescript-language-server
- eslint-lsp
- stylelint-lsp
- null-ls: html/htmldjango, django, css, javascript, jason, jsonc
- tailwindcss
- copilot

**Linter**

- eslint_d
- pyright

**Formatter**

- prettier

**DAP**

- debupy4

**Mason**
以下之 LS Server, Linter 不要安裝：

- pylint
- mypy
