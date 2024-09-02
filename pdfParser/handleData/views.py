from django.shortcuts import render, HttpResponse
import tabula


schema_cols_name = []


def homePage(request):
    try: 
        if (request.method == "POST"):
            uploaded_pdf = request.FILES.get('pdfUpload')
            total_cols = int(request.POST.get('numfields'))
            for i in range(0, total_cols):
                col_name = request.POST.get(f'column{i}')
                schema_cols_name.append(col_name)
            
            # print(uploaded_pdf)


            #getting the data outta pdf file

            dfs = tabula.read_pdf(uploaded_pdf, pages="all", lattice=True)
            for df in dfs: 
                print(df)
    except:
        HttpResponse("error in request method")

    return  render(request,"index.html")