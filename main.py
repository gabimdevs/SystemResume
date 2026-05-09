from output import save_data
from parser import extract_text, extract_email, extract_phone, extract_skills, extract_name

text = extract_text("curriculoGabriela.pdf")

data = {
    "email": extract_email(text),
    "name": extract_name(text),
    "phone": extract_phone(text),
    "skills": extract_skills(text)
}

save_data(data)