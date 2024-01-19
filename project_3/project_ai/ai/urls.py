from django.urls import path

from ai.views import view_about, view_services, view_index, view_features, view_projects, view_team, view_testimonials, \
    view_faq, view_contact, view_404, add_person, list_person

urlpatterns = [
    path('', view_index, name="ap"),
    path('about', view_about, name="about"),
    path('service', view_services, name="service"),
    path('feature', view_features, name="feature"),
    path('project', view_projects, name="project"),
    path('team', view_team, name="team"),
    path('testimonial', view_testimonials, name="testimonial"),
    path('faq', view_faq, name="faq"),
    path('contact', view_contact, name="contact"),
    path('404', view_404, name="Not_found"),
    path('add', add_person, name="add"),
    path('list', list_person, name="list"),
]
