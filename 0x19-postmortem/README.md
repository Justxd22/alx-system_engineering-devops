# Postmortem

![robot confused](Gemini_Generated_Image_b1mey5b1mey5b1me.jpg)

## Issue Summary:
#### Duration:
- The outage lasted from May 09, 2024, 10:00 UTC to May 09, 2024, 11:00 UTC.
#### Impact:
- During this period, WordPress was down as Apache was returning 500 errors to all incoming requests. This affected roughly 100% of requests, leading to major functionality issues and a non-working Wordpress website.
#### Root Cause:
- The root cause was traced using strace to a misconfiguration in the word press config rules within the Apache config files, which led to improper request routing and excessive 500 errors under normal traffic conditions.




## Timeline:
- 10:00 UTC - Automated monitoring tools at DataDog detected an unusually high rate of 500 errors from apache logs.
- 10:05 UTC - Warning emails were sent to the team from DataDog about the High number of errors.
- 10:10 UTC - The team started investigating the root cause of the 500 error codes.
- 10:30 UTC - A recent configuration was detected that caused a misconfiguration in one of the important files for the WordPress website.
- 10:40 UTC - The affected file had a typo that resulted in such errors.
- 11:00 UTC - All systems were up operating and 100% working.

![server crying](Gemini_Generated_Image_b1mey3b1mey3b1me.jpg)





## Root cause and resolution:
- Root Cause: The outage was caused by a misconfiguration introduced during a recent system update that had a typo.
- Resolution: The issue was resolved by resolving the typo and rolling out a Puppet fix for all the running hosts.



![idea](Gemini_Generated_Image_b1mey7b1mey7b1me.jpg)


## Corrective and preventative measures:
### Improvements:
- Constant reviews should be done by the team to avoid such downtime.
- Enhance monitoring capabilities to detect and alert misconfigurations.
### Tasks:
- Task 1: Implement Testing systems before deploying May 11, 2024
- Task 2: Improve monitoring tools to detect such misconfigurations in the feature May 11, 2024.
