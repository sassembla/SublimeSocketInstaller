//
//  AppDelegate.m
//  SublimeSocketInstaller
//
//  Created by sassembla on 2013/06/04.
//  Copyright (c) 2013年 KISSAKI Inc,. All rights reserved.
//

#import "AppDelegate.h"
#import "KSMessenger.h"

#define ST_PATH (@"/Library/Application Support/Sublime Text 2/Packages")
#define SUBLIMESOCKET_PATH  (@"/SublimeSocket")


@implementation AppDelegate {
    KSMessenger * messenger;
}

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    messenger = [[KSMessenger alloc]initWithBodyID:self withSelector:@selector(receiver:) withName:@"INSTALLER"];
    
    NSString * targetPath = [[NSString alloc] initWithFormat:@"%@%@", NSHomeDirectory(), ST_PATH];
    
    [_installTargetPathText setTitle:targetPath];
}

- (void) receiver:(NSNotification * )notif {
    NSDictionary * dict = [messenger tagValueDictionaryFromNotification:notif];
    
    switch ([messenger execFrom:[messenger myName] viaNotification:notif]) {
        case 0:{
            NSTask * task = dict[@"task"];
            
            //wait
            [task waitUntilExit];
            
            [self installed];
            break;
        }
            
        default:
            break;
    }
}

int state = STATE_INITIALIZED;


- (IBAction)tapped:(id)sender {
    
    switch (state) {
        case STATE_INITIALIZED:{
            
            [_loadingText setTitle:@"installing..."];
            [_InstallingIndicator setHidden:NO];
            [_InstallingIndicator startAnimation:self];
          
            [_installlButton setEnabled:NO];
            
            //install先フォルダの確認
            NSFileManager * fMan = [[NSFileManager alloc]init];
            NSString * targetPath = [[NSString alloc] initWithFormat:@"%@%@", NSHomeDirectory(), ST_PATH];

            BOOL isDir;
            
            if ([fMan fileExistsAtPath:targetPath isDirectory:&isDir]) {
                if (isDir) {
                    //OK
                    
                    NSString * installTargetPath = [[NSString alloc]initWithFormat:@"%@%@%@", NSHomeDirectory(), ST_PATH, SUBLIMESOCKET_PATH];
                    //すでにインストールしてあるかどうか
                    if ([fMan fileExistsAtPath:installTargetPath isDirectory:&isDir]) {
                        //フォルダかファイルがある。
                        if (isDir) {
                            [self setInstallFailed:@"Already installed."];
                        } else {
                            [self setInstallFailed:@"Already installed. but file found."];
                        }
                        break;
                    }
                    
                } else {
                    //ファイルがあるwww どうもできん。　
                    [self setInstallFailed:@"There is \"Packages\" file, not folder...\nPlease re-install SublimeText."];
                    break;
                }
            } else {
                //STが無い
                [self setInstallFailed:@"No SublimeText found.\nPlease visit http://www.sublimetext.com and install."];
                break;
            }
            
            NSTask * task = [self install];
            
            [messenger callMyself:0,
             [messenger tag:@"task" val:task],
             [messenger withDelay:0.0001],
             nil];

            break;
        }
            
        case STATE_INSTALLED:{
            exit(1);
            break;
        }
        case STATE_INVALID:{
            exit(1);
            break;
        }
            
        default:
            break;
    }
}

- (void) setInstallFailed:(NSString * )message {
    state = STATE_INVALID;
    [_InstallingIndicator stopAnimation:self];
    [_loadingText setTitle:@"installation failed."];
    
    [_redButton setHidden:NO];
    [_errorText setTitle:message];
    
    [_installlButton setTitle:@"Quit"];
    [_installlButton setEnabled:YES];
}

- (NSTask * ) install {
    //install
    NSTask * task = [[NSTask alloc]init];
    
    NSString * resourcePath = [[NSString alloc]initWithFormat:@"%@%@", [[NSBundle mainBundle] bundlePath], SUBLIMESOCKET_PATH];
    
    NSString * targetPath = [[NSString alloc] initWithFormat:@"%@%@", NSHomeDirectory(), ST_PATH];
    
    //コピーを行う
    [task setLaunchPath: @"/bin/cp"];
    [task setArguments:@[@"-R", resourcePath, targetPath]];
    [task launch];
    
    return task;
}

- (void) installed {
    [_InstallingIndicator stopAnimation:self];
    [_greenButton setHidden:NO];
    [_loadingText setTitle:@"installed."];
    
    [_installlButton setTitle:@"Close"];
    [_installlButton setEnabled:YES];
    state = STATE_INSTALLED;
}

- (void) dealloc {
    [messenger closeConnection];
}

@end
