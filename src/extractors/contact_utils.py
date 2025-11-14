thonimport re

def extract_contacts(html: str):
    emails = list(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
    facebook = list(set(re.findall(r"https?://(?:www\.)?facebook\.com/[A-Za-z0-9_.-]+", html)))
    linkedin = list(set(re.findall(r"https?://(?:www\.)?linkedin\.com/[A-Za-z0-9_/.-]+", html)))
    twitter = list(set(re.findall(r"https?://(?:www\.)?twitter\.com/[A-Za-z0-9_]+", html)))

    return {
        "emails": emails,
        "facebooks": facebook,
        "linkedIns": linkedin,
        "twitters": twitter
    }