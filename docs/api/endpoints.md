For api overview and usages, check out [this page](overview.md).

[TOC]

# Authentication
All api calls are authenticated unless otherwise stated.

## Login

```
POST /api/auth/login  (not authenticated)
```

__Parameters__

Name     | Description
---------|-------------------------------------
email    | email of the user. 
password | password of the user.

__Request__
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

__Response__
```json

Status: 200 OK
{
    "auth_token": "eyJ0eXAiOiJKV1QiL",
    "email": "ak123@fueled.com",
    "id": "f9dceed1-0f19-49f4-a874-0c2e131abf79",
    "first_name": "",
    "last_name": ""
}
```

## Register

```
POST /api/auth/register   (not authenticated)
```

__Parameters__

Name     | Description
---------|-------------------------------------
email    | email of the user. Errors out if email already registered.
password | password of the user.

__Request__
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

__Response__
```json

Status: 201 Created
{
    "auth_token": "eyJ0eXAiOiJKV1QiLCJh",
    "email": "test@test.com",
    "id": "f9dceed1-0f19-49f4-a874-0c2e131abf79",
    "first_name": "",
    "last_name": ""
}
```

## Change password

```
POST /api/auth/password_change
```

__Parameters__

Name             | Description
-----------------|-------------------------------------
current_password | Current password of the user.
new_password     | New password of the user.

__Request__
```json
{
    "current_password": "NotSoSafePassword",
    "new_password": "VerySafePassword0909"
}
```

__Response__
```
Status: 204 No-Content
```


## Request password for reset

Send an email to user if the email exist.

```
POST /api/auth/password_reset   (not authenticated)
```

__Parameters__

Name  | Description
------|-------------------------------------
email | (required) valid email of an existing user.

__Request__
```json
{
    "email": "hello@example.com"
}
```

__Response__
```json

Status: 200 OK
{
    "message": "Further instructions will be sent to the email if it exists"
}
```


## Confirm password reset

Confirm password reset for the user using the token sent in email.

```
POST /api/auth/password_reset_confirm   (not authenticated)
```

__Parameters__

Name          | Description
--------------|-------------------------------------
new_password  | New password of the user
token         | Token decoded from the url (verification link)


__Request__
```json
{
    "new_password": "new_pass",
    "token" : "IgotTHISfromTHEverificationLINKinEmail"
}
```

__Response__
```
Status: 204 No-Content
```

__Note__
- The verification link uses the format of key `password-confirm` in `FRONTEND_URLS` dict in settings/common.


# Current user actions

## Get profile of current logged-in user
```
GET /api/me
```

__Response__

```json
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "first_name": "John",
    "last_name": "Hawley",
    "email": "john@localhost.com"
}
```

## Update profile of current logged-in user
```
PATCH /api/me
```

__Example__
```json
{
    "first_name": "James",
    "last_name": "Warner"
}
```

__Response__

```json
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "first_name": "James",
    "last_name": "Warner",
    "email": "john@localhost.com",
}
```

# TODOS

# Create a todo

Name  | Type | Description
------|------|-------------------
id    | string/uuid| unique id for the todo
todo  | string |todo name
description | string | description for the todo to be completed
is_completed | boolean | Signifies whether the todo is completed
created_at | string/datetime | Date and time when the todo was created
modified_at | string/datetime | Date and time when the todo was modified

__Request__
```
POST /api/todos
```
__Parameters__

Name          | Required     |Description
--------------|--------------|-----------------------
todo          |     y        | Name of the todo
description   |     n        | description of the todo

```
{
    "todo": "Read SICP",
    "description": ""
}
```

__Response__
```
Status 201 Created
```
```
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "todo": "Read SICP",
    "description": "",
    "is_completed": false,
    "created_at": "2019-01-13T14:27:24.505222Z",
    "modified_at": "2019-01-13T14:27:24.505222Z"
}
```

# Retrieve all todos for user

__Request__
```
GET /api/todos
```

__Response__
```
Status 200 OK
```
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
        "id": "4903c586-1696-4bf2-8e61-3df2c1547549",
        "todo": "Read SICP",
        "description": "",
        "is_completed": true,
        "created_at": "2019-01-13T14:27:24.505222Z",
        "modified_at": "2019-01-13T14:27:24.505238Z"
        }
    ]
}
```

# Retrieve a specific todo for a user

__Request__
```
GET /api/todos/:id
```

__Response__
```
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "todo": "Read SICP",
    "description": "",
    "is_completed": true,
    "created_at": "2019-01-13T14:27:24.505222Z",
    "modified_at": "2019-01-13T14:27:24.505222Z"
}
```

# Patch a todo

__Request__
```
PATCH /api/todos/:id
```
```
{
    "is_completed": true
}
```

__Response__
```
Status 200 OK
```
```
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "todo": "Read SICP",
    "description": "",
    "is_completed": true,
    "created_at": "2019-01-13T14:27:24.505222Z",
    "modified_at": "2019-01-13T14:27:24.505222Z"
}
```

# Delete a todo
__Request__
```
DELETE /api/todos/:id
```

__Response__
```
Status 204 No Content
```