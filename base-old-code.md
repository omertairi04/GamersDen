<!--<div id="mySidepanel" class="sidepanel">
                    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                    <p class="username-l">Hi {{ user.username }}</p>
                    <a href="{% url 'gamers:show_profile_page' users.profile.id %}">Go to account</a>
                    <a href="/update_account/">Update Profile</a>
                    <a href="#">News</a>
                    <a href="/create-post/">Post Content</a>
                    <form class="logout-link" action="{% url 'gamers:logout' %}" method="post">
                        {% csrf_token %}
                        <button class="logout" type="submit">Log Out</button>
                    </form>
                  </div>
                <img class="avatar"src="{{ user.profile.image.url }}"
                 width="50px" height="50px" onclick="openNav()">
            </div>
            <a href="{% url ':login' %}">Login</a></li>
                {% else %}-->