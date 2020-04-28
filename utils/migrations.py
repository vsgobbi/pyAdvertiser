from models.user import User


class ModelMigration(object):

    @classmethod
    def addDefaultPermission(cls):

        kwargs = {
            "taxId": "33.549.327/0001-76",
            "email": "none@none.com",
            "fullName": "Pedrão Py Tester",
            "phoneNumber": "99125550156",
            "permissions": ["owner"]
        }
        try:
            user = User.updateItem(**kwargs)
            print(User.json(user))
            return "sucesso"
        except Exception as error:
            return "Não foi possível atualizar.../n {}".format(error)


print(ModelMigration.addDefaultPermission())
