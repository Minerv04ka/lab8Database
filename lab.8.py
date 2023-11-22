from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lab8.db', echo=True)
Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, Sequence('contact_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def create_contact():
    name = input("Введіть ім'я: ")
    email = input("Введіть електронну адресу: ")
    contact = Contact(name=name, email=email)
    session.add(contact)
    session.commit()

def get_all_contacts():
    contacts = session.query(Contact).all()
    return contacts

def update_contact():
    contact_id = int(input("Введіть ID контакту, який потрібно оновити: "))
    new_name = input("Введіть нове ім'я: ")
    new_email = input("Введіть нову електронну адресу: ")
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.name = new_name
        contact.email = new_email
        session.commit()
    else:
        print("Контакт не знайдено.")

def delete_contact():
    contact_id = int(input("Введіть ID контакту, який потрібно видалити: "))
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        session.delete(contact)
        session.commit()
    else:
        print("Контакт не знайдено.")

if __name__ == "__main__":
    while True:
        print("\n1. Додати контакт")
        print("2. Показати всі контакти")
        print("3. Оновити контакт")
        print("4. Видалити контакт")
        print("5. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            create_contact()
        elif choice == '2':
            contacts = get_all_contacts()
            print("\nВсі контакти:")
            for contact in contacts:
                print(f"{contact.id}: {contact.name} - {contact.email}")
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть від 1 до 5.")
