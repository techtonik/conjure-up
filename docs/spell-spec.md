For anything that needs to be done after the applications are deployed in order to have a working stack, 
we recommend breaking up this post-processing into separate individually-understandable steps to help users of your spell learn what is required to get up and going.
For example, one step in an OpenStack spell would import images into Glance, and another would set up Neutron networks.

These steps are defined via shell scripts and metadata files in a sub-directory **conjure/steps**.
The scripts must be named `step-N*.sh` , e.g. **step-01-glance.sh**, **step-02-keystone.sh**, and so on. They will be executed serially in lexicographic order.


There are two reserved filenames for handling special events:

For **post bootstrap**  events, **00_post-bootstrap.sh** is where to do any modifications to the environment or system before deploying charms.

**00_deploy-done.sh** is a required script that is run periodically to check if the deployment is complete. This script should check juju unit status as well as higher-level status, such as internal API endpoint responsiveness.

Here's a basic example that just checks juju unit status:
```
#!/bin/bash

. /usr/share/conjure-up/hooklib/common.sh

while [ $(unitStatus keystone 0) != "active" ]; do sleep 3; done
exposeResult "Keystone available" 0 "true"
```

## Step Metadata

The metadata contains information that describes the step and if there is additional input required. In order for **conjure-up** to pick up the steps metadata the filename needs to be named the same as the step with an extension of **yaml**. For example, if the step filename is **step-01-glance_import_images.sh** the metadata filename would be **step-01-glance_import_images.yaml**. The format for the metadata is as follows:

- **title:** - Single line title
- **description:** - A short description, can be multi line.
- **shortcmd:** - (optional) A short command that shows what this step does. This should normally be `juju action` provided by the charm being accessed by this step.
- **viewable:** Is this step viewable in the UI? Must be set in order to be presented during processing step phase and for allowing users to enter input.
- **runnable:** Is this step runnable? Regardless of if presented to user for additional input this step runs unconditionally.
- **additional-input**: A list of additional inputs that can be answered during processing of each step, the keys required in each input item
  - **label** - The UI label presented to the user, should be a friendly name like, eg. First Name
  - **key** - Unique key of the input to be referenced during processing
  - **type** - Type of input. Valid inputs: text, boolean, integer, password
  - **default** - (optional) Default value

## Example

This example show a step that is presented to the user for additional input.

```yaml
title: Add user
description: Add a user
shortcmd: juju action do punt cat
viewable: True
additional-input:
 - "label": "Username"
   "key": "USERNAME"
   "type": "text"
   "default": "ubuntu"
 - "label": "Password"
   "key": "PASSWORD"
   "type": "password"
```

This example is a step that isn't presented, however, is still run in order of step execution


```yaml
title: Add user
description: Add a user
shortcmd: juju action do punt cat
viewable: False
runnable: True
```
