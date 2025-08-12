# Django Rest Framework API 🚀  
**API REST construida con Django REST Framework**  

Solución robusta para backend con buenas prácticas que implementa autenticación JWT, manejo de relaciones complejas y optimización de queries.

## 🌟 Características Principales

🔹 **Autenticación Segura**: JWT con refresh tokens  
🔹 **Documentación Automática**: Generada con Swagger/OpenAPI  
🔹 **Optimización DB**: Prefetching y select_related integrados  
🔹 **Validación Avanzada**: Serializers personalizados para cada endpoint  
🔹 **Paginación Custom**: Sistema híbrido (limit/offset + cursor)  

## 🛠 Stack Tecnológico  

| Componente       | Tecnologías/Librerías                |
|------------------|--------------------------------------|
| Core             | Python 3.10+, Django 4.2+           |
| API Framework    | Django REST Framework 3.14           |
| Autenticación    | SimpleJWT                            |
| Documentación    | drf-yasg                             |
| Base de Datos    | PostgreSQL (con psycopg2)            |
| Caching          | Redis (django-redis)                 |
| Testing          | pytest-django, factory_boy           |

## 🚀 Instalación Rápida

1. **Clonar repositorio**:
```bash
git clone https://github.com/matias-bello-rodriguez/drf.git
cd drf
```
2. **Configurar entorno virtual**
```bash   
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
3.**Instalar dependencias**
```bash   
pip install -r requirements.txt
```
##⚙ Configuración

1. **Crear y configurar un archivo .env**
```bash   
SECRET_KEY=tu_django_secret_key
DB_NAME=drf_db
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
REDIS_URL=redis://localhost:6379/0
```
2. **Migrar**
```bash
python manage.py migrate
```
## Ejecución

**Server de desarrollo**
```bash
python manage.py runserver
```

**Acceso a la documentacion**
```bash
http://localhost:8000/swagger/
http://localhost:8000/redoc/
```

