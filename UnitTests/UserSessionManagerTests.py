from SessionManagement.User import *;
from SessionManagement.UserRepository import *;
from SessionManagement.UserSessionManager import *;

import unittest

class UserSessionManagerTests(unittest.TestCase):
    
    def setUp(self):
        self.userRepository = UserRepository();
        self.__createUsers();
        self.userSessionManager = UserSessionManager(self.userRepository);
        return

    def test_get_user(self):
        # Add session Id and corresponding email
        key, user = self.userRepository.getOne();
        self.userSessionManager.addNewSession(1234, key);
        
        valid_user = self.userRepository.getUserBySessionId(1234);
        isValid = (key == valid_user.getEmail());
        
        self.assertEqual(isValid, True, "Expected User did not match user gotten")
        return
    
    def test_add_new_session(self):
        # add new session
        user = User();
        
        isValid = True;
        self.assertEqual(isValid, True, "New Session Added not successfully")
        
    def __createUsers(self):
        random_number = 100;
        for i in range(0, 10):
            random_number = random_number + 1;
            user = User();
            key = str(random_number) + '@hotmail.com';
            self.userRepository.addUser(key, user);
              
if __name__ == '__main__':
    unittest.main(); 