## Daily updates.

### Day - 1.

- Done with basic CRUD operation using Django Rest Framework.
	- Using simple Function base views.
	- Using simple Class base views.
- Understood what are Model Serializers and normal Serializers.
- Understood and learned ModelSerializers validations.
	- field level validation.
	- object level validation.
	- Field validators.
- Understanding and learning CRUD operation in DRF 
	- Using Function api_views.
	- Using Class api_views.


### Day - 2.

- Done CRUD operation with Generic APIView and MIXINS in DRF.
	- list()
	- create()
	- retrieve()
	- update()
	- destroy()
- Done CRUD operation with Concrete View Class in DRF.
	- ListAPIView()
	- CreateAPIVuew()
	- RetrieveAPIView()
	- UpdateAPIView()
	- DestroyAPIViw()
	- ListCreateAPIView()
	- RetrieveUpdateAPIView()
	- RetrieveDestroyAPIView()
	- RetrieveUpdateDestroyAPIView()
- Done CRUD Operation with ViewSet in DRF.
	- ModelViewSet.
	- ReadOnlyModelViewSet.

### Day - 4
- Authentication.
	- Basic.
	  - Using username and password.
	- Session.
	  - Creating session and using session ID.
	- Token.
		- Creating Token.
- Permission.
	- AllowAny.
  	- IsAuthenticated.
  	- IsAdminUser.
  	- IsAuthenticatedOrReadOnly.
  	- DjangoModelPermissions.
  	- DjangoModelPermissionsOrAnonReadOnly.
  	- DjangoObjectPermissions.
  	- Custom permissions. 	

- Different methods to generate token.
	- Using admin portal.
	- Using drf_create_token command.
	- Using API endpoint.
	  	- using obtain_auth_token view.
		- inheriting ObtainAuthToken class(custom).
	- Using Signals.
- Custom Authentication.
