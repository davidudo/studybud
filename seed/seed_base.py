'''
  Copy this code and run it using
  >>>python manage.py shell
'''

from django_seed import Seed

seeder = Seed.seeder()

from base.models import User, Topic, Room, Message
seeder.add_entity(User, 20)
seeder.add_entity(Topic, 20, {
    'name': lambda x: seeder.faker.word(),
})
seeder.add_entity(Room, 40)
seeder.add_entity(Message, 200)

inserted_pks = seeder.execute()
