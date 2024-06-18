from dishka import Provider, Scope, provide
from g4f.client import Client

class G4FProvider(Provider):
   
    @provide(scope=Scope.APP)
    def g4f_client(self) -> Client: 
        return Client()

