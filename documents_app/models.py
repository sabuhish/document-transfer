from django.db import models
from companies_app.models import Company

class Documents(models.Model):
    __choice =((1, "yarandi"),
    (2, "gonderen imzaldir"),
    (3, "qebul eden imzaldir"),
    (4, "qebul eden imtina etdi"),
    (5, "vaxti bitib"))
    __doct_type_choice = ((1, "muqvile"),
    (2, "hesab_faktura"))
    sender = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sender_doc_set")
    reciever = models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name="receiver_cod_set")
    notes =models.CharField(max_length=255, verbose_name="qeydler")
    doc_date =models.DateField()
    doc_expr_date =models.DateField()
    status = models.IntegerField(choices=__choice, default=1)
    doc_send_date = models.DateTimeField(auto_now=True)
    doc_file= models.FileField(upload_to="docs")
    doc_type = models.IntegerField(choices=__doct_type_choice)