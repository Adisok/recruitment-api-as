# RECRUITMENT_API/DOCS
## Link do API:
https://recruitment-app-as.herokuapp.com/

## POST /token 
Wykorzystuje metodę post do Basic Auth, który generuje token uwierzytelniający, dla użytkownika, następnie trzeba ten Token podawać przy tworzeniu, edycji i kasowaniu wiadomości.
W zapytaniu należy zawrzeć nazwę użytkownika i hasło, obecnie jest zdefiniowany tylko jeden użytkownik :
requests.post("Link do API /token", auth=("Daft_user", "Daft_Password"))

Co Zwróci:
"api_token": "BASIC2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"

## POST /create_msg
Endpoint służący do tworzenia wiadomości. Przyjmuje jsona o następującym formacie:
{
    "MessageText": "string",
    "Token": "BASIC2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"
}

I zwraca następującego jsona:
{
  "MessageID": 1,
  "MessageText": "string",
  "Counter": 1,
  "Token": NULL
}

Przykładowe zapytanie:
```python
requests.put(f" Link do API /edit_msg/{TEST_ID}", json=test_edit)
```


## PUT /edit_msg/{msg_id}
Metoda służy do edycji wiadomości. Należy podać msg_id (ID wiadomości) oraz następującego jsona:

{
  "Message": "string",
  "Token": "BASIC2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"
}

Co zwróci:
{
  "MessageID": 1,
  "MessageText": "string",
  "Counter": 1,
  "Token": NULL
}

Przykładowe zapytanie:
```python
requests.put(f" Link do API /edit_msg/{TEST_ID}", json=test_edit)
```

## DELETE /delete_msg/{msg_id}
Służy do usuwania wiadomości o podanym ID. Poza ID należy podać również jako params Token.
Przykładowe zapytanie:
```python
requests.delete(f" Link do API /delete_msg/{TEST_IDE}", params={"auth": TOKEN})
```

## GET /info_msg/{msg_id}
Wyświetla wiadomość i licznik o podanym ID. 
```python
requests.get(f{ Link do API /info_msg/{TEST_ID}")
```
## API Deploy
Api zdeployowano na heroku. Połączono heroku z moim repo na githubie automatycznie aktualizując API przy każdym commicie. 
Bazę danych danych najpierw ręcznie stworzono lokalnie po czym wrzucono na githuba dumpa, który został użyty do backupa bazy danych na heroku.

## BAZA DANYCH
TABEL: content
ROWS : MessageID | MessageText | Counter
