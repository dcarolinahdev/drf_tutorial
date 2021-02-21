# Working with DjangoRestFramework

## 1. Models

## 2. Serializers

```
The first part of the serializer class defines the fields that get serialized/deserialized. The **create()** and **update()** methods define how fully fledged instances are created or modified when calling **serializer.save()**.

A serializer class is very similar to a **Django Form class**, and includes similar validation flags on the various fields, such as **required**, **max_length** and **default**.
```

> The **{'base_template': 'textarea.html'}** flag above is equivalent to using widget=widgets.Textarea on a Django Form class. 

```
We can actually also save ourselves some time by using the ModelSerializer class, as we'll see later, but for now we'll keep our serializer definition explicit.
```
