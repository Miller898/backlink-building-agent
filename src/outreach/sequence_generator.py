thondef generate_sequences(title: str, description: str, url: str):
email_sequence = [
{
"subject": f"Potential Collaboration Opportunity: {title}",
"preview": f"Reached out regarding {title.lower()}",
"text": (
f"Hi,\n\nI recently reviewed your article titled '{title}'. "
f"It offers strong insights and I believe there's an opportunity "
f"for collaboration.\n\nHere’s the link I found: {url}\n\n"
f"Would you be open to discussing backlink or partnership opportunities?\n\nThanks!"
)
}
]

return {
"email": email_sequence,
"social": {
"linkedin": f"Hi! Loved your article '{title}'. Are you open to collaboration?",
"twitter": f"Great read on '{title}'! DM to discuss a backlink opportunity?",
"facebook": f"Hi! Found your article '{title}'. Interested in collaborating on content?"
}
}