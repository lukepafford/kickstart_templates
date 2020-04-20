kickstart_templates
===================

Simple flask server used to render an opinionated kickstart file for Centos 8.
The server reads your custom `data.json` file and renders the kickstart response.

The kickstart expects to be integrated with AWX, and RedHat IDM.
The goal is to create a VM and automatically register itself with AWX.

the `hostname` variable must be provided as a query argument.


## Expected context variables
*	`root_crypted_password`: $6$ADF2837aDK...
*	`admin_crypted_password`: $6$zlDK20dk...
*	`admin_user`: first.last
*	`install_url`: http://mirror.centos...
*	`drive_type`:  (vda/sda)
*	`domain`: example.com
*	`idm_server`: idm.example.com
*	`idm_api_username`: idm_admin
*	`idm_api_password`: idm_password
*	`awx_token`:  DK29d8AKDf...
*	`awx_base_url`: http://awx.example.com:5000
*	`awx_inventory_update_job_id`: 5
*	`awx_callback_job_id`: 6
