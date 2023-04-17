![alt text](https://chainstack.com/wp-content/uploads/2019/03/Logo-Blue@3x-Padded.png?raw=true)

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Content table
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introduction</a></li>
  <li><a href="#implementacion-del-proyecto">Project implementation</a></li>
  <li><a href="#iniciar-aplicacion">Run application</a></li>
  <li><a href="#comandos-utiles">Util commands</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introduction</h2>

The project is a platform with an authentication and authorization system that allows users to create, list, and delete resources while ensuring that they cannot access other users' resources. The platform also includes a quota system to limit the number of resources each user can create. Administrators have the ability to manage users, including their resources and quotas. The platform uses Swagger to automatically document its APIs.

<h2><a id="user-content-implementacion-del-proyecto" class="anchor" aria-hidden="true" href="#implementación-del-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Project implementation</h2>
<ul>
<li><strong>Python</strong>: Programming language utilized.</li>
<li><strong>Django</strong>: Open-source framework.</li>
<li><strong>Django REST Framework</strong>: Django application to build a REST architecture.</li>
<li><strong>PostgreSQL</strong>: Database engine.</li>
<li><strong>Postman</strong>: To test the app.</li>
<li><strong>Docker</strong>: For the deployment of the app.</li>
</ul>

Authentication and session system with tokens, and these tokens have their own expiration time. 

I use Swagger to automatically document the APIs of the platform.

<h2><a id="user-content-iniciar-aplicacion" class="anchor" aria-hidden="true" href="#iniciar-aplicacion"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Run application</h2>

<p>You will need this dependencies to run the project:</p>
<ul>
    <li><a href="https://docs.docker.com/get-docker/" rel="nofollow">Docker</a>.</li>
    <li><a href="https://docs.docker.com/compose/install/" rel="nofollow">Docker compose</a>.</li>
</ul>

<br>


Build the cointainers:

<pre><code>sudo docker-compose build
</code></pre>

Run the app:

<pre><code>sudo docker-compose up
</code></pre>

<h2><a id="user-content-comandos-utiles" class="anchor" aria-hidden="true" href="#comandos-utiles"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Util commands</h2>
<br>
<br>
<strong>Create admin user:</strong>
<br>
<br>
Allows you to create an Admin user yo can access to /admin and you will have higher permissions.
<br>
<br>
<pre><code>docker ps
docker exec -it 32c743258eaa sh
python manage.py createsuperuser --email=nico@example.com
exit
</code></pre>

<em>
  Tip: You have to follow the instructions.
</em>

<br>
<br>
<strong>Testing:</strong>
<br>
<br>
I implemented coverage for testing, you can run the tests with the following commands.
<br>
<br>
<pre><code>docker ps
docker exec -it 32c743258eaa sh
coverage run --source='.' manage.py test
coverage report
</code></pre>
<em>
    Tip: You must be inside the docker shell to run this.
</em>

<br>
<br>
<strong>Endpoints information:</strong>
<br>
<br>
You can have a better information about the endpoints with:
<br>
<br>

### `http://127.0.0.1:8000/swagger/`
### `http://127.0.0.1:8000/redoc/`

