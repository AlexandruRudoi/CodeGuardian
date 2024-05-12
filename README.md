# CodeGuardian

CodeGuardian is a web app for plagiarism detection in source code that is free to use.

All you need is a browser. No additional installations needed. We describe the steps for plagiarism detection within a set of source files.

## Upload and inspect source files

Start plagiarism detection by uploading a ZIP-file containing the source files you want to inspect.

[Screenshot of the upload form]

Specify a name for the analysis or keep the default name. This name allows you to identify results in the backlog of analysis results that is kept in your browser history.

CodeGuardian automatically detects the programming language of the inspected source files based on their file extensions. If the ZIP-file contains source files from a mix of programming languages, CodeGuardian will only inspect the files from the dominant programming language. Select a specific programming language if you want to override the automatic selection.

Read the terms and conditions and check "I accept the above conditions".

Click "Analyze" to upload your files and start the analysis.

**TIP:** You can enhance the analysis results by adding metadata to your submissions. Submissions exported with the option Include info csv enabled already include metadata in a format CodeGuardian recognizes.

## Analysis results

CodeGuardian schedules an analysis for your submitted dataset. The scheduler uses a queue to avoid overloading the server. You get informed as soon as the analysis is completed:

[Notification if the analysis is complete]

Click "View results" to start exploring the analysis results.

[Screenshot of the report page]

## Sharing reports

By default, the secret link to your analysis report is kept hidden, so you don't accidentally share it with others.

To share a report, click the "Share" button in the top right corner and copy the secret link.

## Report history

To the right side of the upload form, you'll see a list of previous analysis results. This list is stored in the local storage of your browser, meaning that the list is removed whenever you clear your browser data.

[Screenshot of the report history list]

If you want to keep track of a report or share it with someone else, click the "Share" button and copy the secret link.

If you want to permanently delete a submitted dataset and its analysis report from our servers, click the "Delete" button.

**INFO:** If the secret link to a report gets lost (for example: by clearing your browser data), you can no longer delete the report from our servers yourself. However, the secret link is the only way to get access to the report and we periodically delete old reports from our servers. You can simply upload the same dataset again to generate a new report.
