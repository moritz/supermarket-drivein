This is a backend for a drive-in supermarket app, developed in the [#WirVsVirus hakcathon](https://wirvsvirushackathon.org).

It is a super early prototype, and should not be considered for production use.

## Usage

You can currently access the following resources:

### Category

A category is used to classify a merchant.

Examples include "Lebensmittel", "Drogerie".

A category has an `id` (unique identifier, integer) and a name (string, also unique).

#### Listing

You can get a list of categories like this:

https://drivein.moritzlenz.de/category

### Merchant

A merchant is somebody who sells goods.

A merchant has a unique `id` (integer), and the following mandatory attributes:

* `name` (string)
* `address` (string, usually multi line)
* `category` (object, references a category)

as well as the following optional attributes, all of which can be either the designated type or `null`:

* `latitude`, `longitude`: geo coordinates (float)
* `phone_number (string)`: Phone contact for the general public
* `products` (string):  Products that the merchant offers
* `url_website` (string): Link to the merchant's website
* `url_online_shopping` (string): Link to the merchant's online shipping portal
* `out_of_stock` (string): Text describing what the merchant currently doesn't have in stock
* `payment_methods` (string): Text describing what payment methods the merchantsaccepts

#### Listing

You can get a listing of all merchants through this URL:

https://drivein.moritzlenz.de/merchant

#### Creating

You can create a new merchant record by sending a POST request to the URL

https://drivein.moritzlenz.de/merchant

The request must include the attributes `name`, `address` and `category`, and may include any of the optional attributes.

This is an example payload:

    {
        "name": "Bäckerei bei Ida",
        "category": {"name": "Bäcker"},
        "address": "Hans-Böckler-Str 7a\n90765 Fürth",
        "out_of_stock": "Bagels, Brezen",
        "payment_methods": "Bargeld"
    }

Note that `category` must reference an existing category, either by name or by id.

On the command line, you can send the request like this:

    $ curl -X POST --data @merchant.json https://drivein.moritzlenz.de/merchant
    
The return value is an object with the newly created record, including the server-generated ID.

