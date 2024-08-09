from django.shortcuts import render

# Create your views here.
#creating a view for just testing the initiation FEEL FREE TO ERASE IT 

def homePage(request):
    if (request.method == "POST"):
        uploaded_pdf = request.FILES.get('pdfUpload')
        total_cols = int(request.POST.get('numfields'))
        schema_cols_name = []
        for i in range(0, total_cols):
            col_name = request.POST.get(f'column{i}')
            schema_cols_name.append(col_name)
        '''
        saare columns ke naam schema_cols_name array mein aa rahe ab inn names ki help se table bana dio, fir use database mein store main kra
        doonga and FYI ABHI DATABASE CONNECT NHI KIYA HAI
        '''
        print(schema_cols_name)

    return  render(request,"index.html")