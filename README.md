# kivy-stubs-pycharm
Kivy stubs generated by PyCharm

## Usage with VSCode
To use this repository with VSCode, clone this repo and then add the `/path/to/kivy-stubs-pycharm` to `settings.json` under the `"python.analysis.extraPaths"` property.

```javascript
// settings.json
{
// ...
"python.analysis.extraPaths": [
    "/path/to/kivy-stubs-pycharm",
]
}
```

### Before
![image](https://github.com/mwmuni/kivy-stubs-pycharm/assets/25945064/73ffc589-e54e-45c2-9a23-eee7e33553d9)


### After
![image](https://github.com/mwmuni/kivy-stubs-pycharm/assets/25945064/15ffdebd-cd76-4200-b7c1-9eb1e43781e7)

## Troubleshooting
- It's not working, what do I do?
  - DO NOT put `/path/to/kivy-stubs-pycharm/kivy` as this will not work!
  - This was tested using PyLance and MyPy. Try those if you're having trouble.
 
## Additional PyCharm Stubs
If you have more PyCharm stubs for Kivy than this repo, please make a pull request!
