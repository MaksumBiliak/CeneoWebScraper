from wtforms import Form, StringField,SubmitField,validators

class ExtractForm(Form):
    porduct_id = StringField("Product id" , name="product_id", id="product_id",validators=[
        validators.DataRequired(message="Product id is required"),
        validators.Length(min=6, max=10,message="Product id should be have between 6 and characters"),
        validators.Regexp(r'[0-9]*',message="Product id can contain only digits")

    ])
    submit = SubmitField("Extract opinions")
    