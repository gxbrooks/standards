
# Definitions

An automation is a script, playbook, or program used to manage an environment consisting of interacting systems. A system may be an application or an OS on a hardware system. 

An automator is a person or AI that implements an automation. 
An operator is a person or AI that runs automations, but does not have the priviledges to develope production automations. 

A transient automation (typically Linux scripts) are automations created by an AI for a human to run or use for by an AI for focused diagnostc scripts to resolve technical or functional issues within a project. 

# Playbook Pattern for Services

For managing services, we define the following types of playbooks for managing a service:
| **Playbook Name** | **Description** |
| :--- | :--- |
| **build** | Aggregate and artificats needed to build a service and then compoile or transform the artifacts into a form suitable to deploy or install the service |
| **deploy** | Deploys all the resources to a host or container that runs the service |
| **install** | Marshalls all the resources needed for a service onto a control node, a managed node, or a local repopsity |
| **start** | Starts the service on the container or host without having to reinstall or redeploy any resources |
| **diagnose** | Observes and reports current health/state of the service and prerequisites with read-only checks. Sometimes this is called a **status** playbook, but that term is deprecated. |
| **test** | Asserts expected behavior by exercising workflows end-to-end and returning pass/fail results. May create short-lived test artifacts and should clean them up. |
| **stop** | Stops the service running |
| **undeploy** | Removes all the resources needed for a service from a host or container |
| **uninstall** | Removes all transient resources from the control node with the exception of any source code from a repository |

## Per-Verb Semantics

### build
- Purpose: transform source or templates into deployable artifacts.
- Typical behavior: compile, package, render, stage.
- Side effects: artifact outputs only.

### install
- Purpose: prepare hosts and control nodes with prerequisites.
- Typical behavior: install packages, users, directories, runtimes, base configs.
- Difference vs deploy: install prepares substrate; deploy places service resources on that substrate.
- Side effects: host-level state changes expected and persistent.

### deploy
- Purpose: place and configure service-specific resources so the service can be started.
- Typical behavior: apply manifests, distribute configs, create service accounts, mount points.
- Difference vs install: deploy targets service composition; install targets foundational prerequisites.
- Side effects: service artifacts/manifests present, but service may still be stopped.

### start
- Purpose: transition deployed service to running.
- Typical behavior: start daemons, scale workloads up, enable runtime routes.
- Side effects: runtime activity starts.

### diagnose
- Purpose: answer "what is the current state and what is wrong?"
- Behavior characteristics:
- Read-only checks where possible.
- Safe to run repeatedly in broken or healthy environments.
- Reports facts (pods, ports, endpoints, cert dates, mounts, logs).
- Must include all checks in the corresponding test playbook for the same service.
- Must be a superset of the corresponding test playbook by adding deeper diagnostics, richer evidence, and remediation hints.
- May run additional in-depth probes that are heavier than test.
- Preferred outputs:
- Structured table/list of checks with status and details.
- Clear remediation hints for each failed check.

### test
- Purpose: answer "does the service behavior meet expectations?"
- Behavior characteristics:
- Executes workflow assertions (for example write->read, submit->complete, emit->observe).
- Produces explicit pass/fail outcomes suitable for CI or release gates.
- May create temporary test artifacts and should clean them up.
- Should fail fast with actionable diagnostics.
- Relationship to diagnose:
- Test is the baseline check set for service correctness.
- Diagnose includes all test checks plus deeper diagnostic checks.
- A test that wholly depends on another test must not run when the prerequisite test fails.

### stop
- Purpose: transition running service to non-running state without removing deployment artifacts.
- Typical behavior: stop daemons, scale workloads down.

### undeploy
- Purpose: remove deployed service resources from targets.
- Typical behavior: delete manifests/resources, remove service-level configs.

### uninstall
- Purpose: remove installed prerequisites/transient host resources.
- Typical behavior: uninstall packages/services and clean transient state.


# Statements
1. An automator must not store any artifcats in the playbook directories 
1. An automator must put any artifacts in a diretory dedicated to artifacts for a service or a repository (e.g. Docker image libary) that provides a service for specific type of artifacts
1. An automator must deploy only those artifacts needed on a target host onto the targert host
1. An automator must implement playbooks to start and stop the service. 
1. For service management, an automator can only create playbooks named with the names specified in the service management pattern
1. For each role, an automator must create nor more than one playbook that performs the service management role
1. An automator should implemenmt a diagnose playbook
1. An automator, may or may not implement all of the playbooks in the service automation pattern, depending on how the service is built
1. You must fully automate all system configurations so that we can always build from the source of a project. 
1. The automation platform is Ansible. You must use Ansible for all automations, unless the automation is to manage or deploy prerequisite of  
1. An automation should not execute a step unless the step is necessary. Each step should check whether the outcome of the step is already in place and skip the step when it is. For example, do not delete a directory if the directory does not exist, and do not re-apply a configuration that already matches the desired state. You may rely on commands or modules that perform this check internally (for example, most Ansible modules).
1. If an automation cannot test whether a step is necessary (for example, the API does not expose the current state), the automation must emit an informational message that the action is being redone before re-executing the step.
1. Each automation should be idempotent. I.e. rerunning the automation must not have any ill effects and must result in the same configuration state. The primary automation platform is Ansible. 
## Diagnostic and Test Playbooks
1. For a service that has both test and diagnose playbooks, the diagnose playbook must include all checks in the test playbook for that service.
1. A diagnose playbook should include deeper and broader checks than a test playbook for the same service.
1. If a check wholly depends on the success of a prerequisite check, the dependent check must not run when the prerequisite check fails.
1. Shared logic between test and diagnose playbooks should be factored into common reusable tasks or sub-playbooks to avoid duplication.
1. A single-play or single-task check should not be extracted into a separate shared playbook unless reuse and maintenance value clearly outweigh added indirection.

## Transient Scripts
1. A developer should create a top-level tmp directory for each project
1. A developer must add the tmp directory to the .gitignore file
1. Developers must create transient scripts in the tmp directory
1. Developers must not commit transient scripts to a Git repository

## Service Automation
1. An automator must follow the build, install, deploy, start, diagnose, stop, uninstall pattern of playbooks for managing a service.  


## Playbooks

### common directory
1. A service module may contain a `common` subdirectory to hold reusable playbook fragments or task files shared by multiple playbooks such as test and diagnose.
1. Content in a `common` subdirectory should contain only reusable logic and must not change the semantic purpose of the calling playbook.
1. Automators should keep shared code in `common` only when that reduces meaningful duplication and improves consistency of checks across playbooks.

