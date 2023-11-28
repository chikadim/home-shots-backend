# Testing API of HomeShots

Back to the [README.md](README.md)

## Contents
 * [Automated Unit Testing](#unit-testing)
   + [Profile View](#profile-view)


## Automated Unit Testing

<br />


### Profile View
- Created 5 tests to check that a valid id will retrieve a profile, an invalid id will not retrieve a
profile, check if a user can update their own profile and a profile cannot be updated by someone
who doesn't own it.

```
class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_profile(self):
        adam = User.objects.get(username='adam')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        paul = User.objects.create_user(username='paul', password='pass')

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.data['owner'], 'adam')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/profiles/1/', {'name': 'paul'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'paul')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_profile(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/profiles/2/',
            {'owner': 'paul'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

- All tests passed

![Testing prfofile view](/documentation/screenshots/profile-tests.webp)

<a href="#top">Back to the top.</a>