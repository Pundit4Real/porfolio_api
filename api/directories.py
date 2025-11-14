import time


def project_image_directory(instance, filename):
    return "/".join(
        ["images", "projects", f"{str(time.time())}_{instance.slug}_{str(filename)}"]
    )
def about_directory(instance, filename):
    return "/".join(
        ["images", "about", f"{str(time.time())}_{instance.slug}_{str(filename)}"]
    )

def home_directory(instance, filename):
    return "/".join(
        ["images", "home", "profile", f"{str(time.time())}_{instance.slug}_{str(filename)}"]
    )

def home_directory(instance, filename):
    return "/".join(
        ["files", "home", "resume", f"{str(time.time())}_{instance.slug}_{str(filename)}"]
    )
