from django.shortcuts import render, HttpResponse
from django.db import connection, models
import tabula

schema_cols_name = []

def create_dynamic_model(table_name, fields):
    class Meta:
        db_table = table_name

    attrs = {
        'Meta': Meta,
        '__module__': __name__,
    }
    for field in fields:
        attrs[field] = models.CharField(max_length=255)

    model = type(table_name, (models.Model,), attrs)
    return model

def homePage(request):
    global schema_cols_name
    try:
        if request.method == "POST":
            uploaded_pdf = request.FILES.get('pdfUpload')
            total_cols = int(request.POST.get('numfields'))
            table_name = "dynamic_table"

            schema_cols_name = [] 
            for i in range(total_cols):
                col_name = request.POST.get(f'column{i}')
                if col_name:  
                    schema_cols_name.append(col_name)

            print(schema_cols_name)
            if schema_cols_name:
                model = create_dynamic_model(table_name, schema_cols_name)

                with connection.schema_editor() as schema_editor:
                    schema_editor.create_model(model)
                

                #storin our data here
                dfs = tabula.read_pdf(uploaded_pdf, pages="all")
                for df in dfs:
                    for _, row in df.iterrows():
                        row_data = {col: str(row[col]) for col in schema_cols_name if col in df.columns}
                        model_instance = model(**row_data)
                        model_instance.save()
                
                return HttpResponse(f"Table '{table_name}' created successfully with columns: {', '.join(schema_cols_name)} and data inserted.")
            else:
                return HttpResponse("No column names provided, table not created.")

    except Exception as e:
        return HttpResponse(f"Error in request: {str(e)}")  
    return render(request, "index.html")
