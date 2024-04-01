class DocumentInfos:

    title = u'Flight Viewer'
    first_name = 'Emilien'
    last_name = 'Progin'
    author = f'{first_name} {last_name}'
    year = u'2024'
    month = u'avril'
    seminary_title = u'Projet OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/milmip/Flight-Viewer"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()
