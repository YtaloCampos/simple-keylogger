# simple-keylogger
  a simple keylogger with smtp implemented

## Requirements
  * python2.7 or >
  
## How to use

#### Shell mode
  ```
  python ./shell.py --from $email --to $email --pass $password
  ```
  
 * --from - sender email (optional)
 * --to   - recipient email (optional)
 * --pass - sender password (optional)
 
 * press 'F4' to receive the data by email
 * press 'ESC' to close
 
  > A email is optional.
  > A log file will be created in the tmp folder.
  
#### Graphic mode
  ```
  python ./interface.py
  ```
  * press 'F4' to receive the data by email
  * press 'ESC' to close
   
  > Fields only if you want to receive the data in your email.
  > A log file will be created in the tmp folder.
