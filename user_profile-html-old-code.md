<div class="card mb-3">
    <div class="row g-0">
      <div class="col-md-2">
    {% if page_user.profile_pic %}
        <img src="{{ page_user.profile_pic.url }}" class="img-fluid rounded-start" width="250" height="250">
    {% else %}
        <img src="{% static 'GProfile/images/pfp.jpg' %}" class="img-fluid rounded-start" width="250" height="250">
    {% endif %}  
    </div>
      <div class="col-md-10">
        <div class="card-body">
          <h5 class="card-title">{{ page_user.user.username }}</h5>
          <p class="small text-muted">

            {% if page_user.Website %}
                <a href="{{ page_user.Website }}">Website</a> |
            {% endif %}

            {% if page_user.Facebook %}
                <a href="{{ page_user.Facebook }}">Facebook</a> |
            {% endif %}
            {% if  page_user.Twitter %}
                <a href="{{ page_user.Twitter }}">Twitter</a> |
            {% endif %}
            {% if page_user.Instagram %}
                <a href="{{ page_user.Instagram }}">Instagram</a> |
            {% endif %}
            {% if page_user.Steam %}
                <a href="{{ page_user.Steam }}">Steam</a> |
            {% endif %}
            <p class="card-text">{{ page_user.bio }}</p>
        </div>
      </div>
    </div>
  </div>