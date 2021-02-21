# Working with DjangoRestFramework

## 1. Models

## 2. Serializers

```
The first part of the serializer class defines the fields that get serialized/deserialized. The **create()** and **update()** methods define how fully fledged instances are created or modified when calling **serializer.save()**.

A serializer class is very similar to a **Django Form class**, and includes similar validation flags on the various fields, such as **required**, **max_length** and **default**.
```

> The **{'base_template': 'textarea.html'}** flag above is equivalent to using widget=widgets.Textarea on a Django Form class. 

```
We can actually also save ourselves some time by using the **ModelSerializer class**, as we'll see later, but for now we'll keep our serializer definition explicit.

It's important to remember that **ModelSerializer classes** don't do anything particularly magical, they are simply a shortcut for creating serializer classes:

An automatically determined set of fields.
Simple default implementations for the **create()** and **update()** methods.
```

## 3. The views

## 4. The urls

```
It's worth noting that there are a couple of edge cases we're not dealing with properly at the moment. If we send malformed **json**, or if a request is made with a method that the view doesn't handle, then we'll end up with a **500 "server error"** response. Still, this'll do for now.
```
