import time
import hashlib
import os

def hash_filename(slug, filename):
    """Generate a short, unique, and safe filename."""
    timestamp = str(time.time())
    name_hash = hashlib.sha1(f"{slug}_{filename}_{timestamp}".encode()).hexdigest()
    ext = os.path.splitext(filename)[1]  # keep original extension
    return f"{name_hash}{ext}"


def project_image_directory(instance, filename):
    """Project images."""
    filename = hash_filename(instance.slug, filename)
    return os.path.join("images", "projects", filename)


def about_directory(instance, filename):
    """About images."""
    filename = hash_filename(instance.slug, filename)
    return os.path.join("images", "about", filename)


def home_profile_directory(instance, filename):
    """Home profile image."""
    filename = hash_filename(instance.slug, filename)
    return os.path.join("images", "home", "profile", filename)


def home_resume_directory(instance, filename):
    """Home resume file."""
    filename = hash_filename(instance.slug, filename)
    return os.path.join("files", "home", "resume", filename)


def testimonial_directory(instance, filename):
    """Testimonial images."""
    filename = hash_filename(instance.slug, filename)
    return os.path.join("images", "testimonial", filename)
