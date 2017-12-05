from InstagramAPI import Instagram, Checkpoint
from apistar import http, Response


class InstaApi(Instagram):

    def __init__(self, *args, **kwargs):
        super(InstaApi, self).__init__(* args, **kwargs)
        
    def getPhoto(self):
        try:
            self.login()
        except ValueError:
            print(ValueError)
            exit()
        aux = "insta.getSelfUsernameInfo()"
        data = {"res": aux}
        return Response(data, status=200, headers={'location': '/'})