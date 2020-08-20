"""
This file containes the Identified Test-Cases for User Management Portal @https://ankitairen.github.io/

"""

print(

"""


LOGIN PAGE FUNCTIONALITY & UI VALIDATION :

    USABILITY TEST : 
    
        1- Portal is accessible over web Url https://ankitairen.github.io/ - Done
        
        2- Verify that the login screen is having option to enter username and password with submit button  -Done
            and option of forgot/reset password.
        
        3- Element type of testbox "password" on UI should not be text, it should be of type "password". (*****) - Done
        
        4- Verify there should be checkbox with label "remember password" on the login page. - Done
        
        5- user is displayed the message like "incorrect username or password" instead of exact message pointing
            at the field that is incorrect. As message like "incorrect username" will promote hacker in bruteforcing.  
            
        6- Validation of System generated HINT "Password must conatin at least one lower case alphabet, 
            one upper case alphabet, one number and one special character!"  - Done
            
        7- Cross Browser compatibility  - Not Done
            
    POSITIVE - HAPPY PATH TESTS:

    Login : Valid userid: X password: Y

        1- login successful using proprietary data (Both input is correct) - Done
        
        2- Verify the timeout of the login session  - BUG 
        
        3- Verify user is  allowed to log in simultaneously with different credentials in different browser. Done

    NEGATIVE:

    login: [user not registered]

        2- login fail with unregistered user  - Done

    login: [invalid/Wrong password]

        3- User can't log in with correct userid but bad password  -Done
    
    login: [Empty username & empty Password]  
    
        4- User can't log in with blank userid &  password  -Done
    
    login: [Case sensitive validation for Credentials]
        
        5- Login with case changed username /password   -Not Done
            
    login: [credential length Boundary Validation]  - No Error, But User is not being created
    
        6- User exceeds the allowed character limit of the user name and password fields.
        
    login/logout: [navigate back & forth after logout]
    
        7- Verify the login page by pressing "Back button" of the browser. 
            It should not allow you to enter into the system once you log out.   - Bug 

    login: [System unavailability (servers are down, no internet connection)]

        8- User can't log in to system with proprietary login and password.
        
        
USER MANAGEMENT PAGE FUNCTIONAL & UI VALIDATION :


    ADD USER Page :

    1- User should be able to land on Add User page after successful admin login.  - Done

    2- Verify the Menu Bar having different tabs (SignOut, ViewUsers & AddUser) - Done
    
    3- Verify if admin can create a User successfully. (Inclusive of case of not Mandatory field validation) - Done
    
    4- Verify if Admin can Update a non admin User details and it got updated successfully.  - Bug
    
    5- Verify User can login to Portal using newly created User credentials. - Done
    
    6- Verify admin can delete the user created.  - BUG
    
    7- Verify admin can search for specific user using search box .  - Done
    
    8- Verify admin can list out all the user details matching to a particular string expression - Done
    
    9- Column wise Sorting can be performed - Done 
    
    10- User should get error on screen in case of Duplicate UserID is being used.   -Done
        ** This userid already exists. Please enter another userid. **
        
   
    USER PROFILE Page :
    
    1- Verify user other than Admin, on successful login , land on "MyProfile" Page. - Done
    
    2- Verify on the Menu bar, 2 options are visible (MyProfile by Default and SignOut) - Done
    
    3- Verify "UserID" Text box is Greyed Out and no Edit is allowed for text. - Done
     
    4- Verify User can edit all the text box other than "UserID".  - Bug
    
    5- Verify User not allowed to leave "password" textbox Blank during Update.  
    
    6- Verify "Update" button on Page is click able.  - Done
    
    7- Verify updated user details should be shown on screen as soon as User clicks on "Update" button.  - Bug
    
    8- After Updating the Details of a specific user ,Login with Admin and 
       verify admin can see the Updated details on "View User" page.       - Bug
    
    8- User Can sign out from the Page.  - Done
        

"""

)
