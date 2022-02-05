import requests

years = ["2014","2015","2016","2017","2018","2019","2020","2021","2022"]
archivos = ["ENTIDAD","MUNICIPIO","DISTRITO_FEDERAL","DISTRITO_LOCAL","SECCION","LOCALIDAD","MANZANA","LOCALIDADES_URBANAS","LOCALIDADES_RURALES","Area_Servicio_AM","Area_Servicio_FM_AGS_CHIH","Area_Servicio_FM_CDMX_MICH","Area_Servicio_FM_MOR_SLP","Area_Servicio_FM_SIN_ZAC","Area_Servicio_FM_Complementaria","Area_Servicio_TDT","Area_Servicio_TDT_Complementaria"]
for y in years:
    for a in archivos:
        filename =y + "_" + a+".zip"
        link = "https://pautas.ine.mx/transparencia/mapas/cob_" + y + "/" + a + ".zip"
        print(link)
        r = requests.get(link)
        if r.status_code==404:
            continue
        else:
            with open(filename,'wb') as f:
                f.write(r.content)
