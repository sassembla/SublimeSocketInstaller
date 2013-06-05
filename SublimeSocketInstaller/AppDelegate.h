//
//  AppDelegate.h
//  SublimeSocketInstaller
//
//  Created by sassembla on 2013/06/04.
//  Copyright (c) 2013年 KISSAKI Inc,. All rights reserved.
//

#import <Cocoa/Cocoa.h>

enum STATE {
    STATE_INITIALIZED,
    STATE_INSTALLED,
    STATE_INVALID
};

@interface AppDelegate : NSObject <NSApplicationDelegate> {
    __weak NSProgressIndicator *_InstallingIndicator;
    __weak NSButton *_greenButton;
    __weak NSButton *_redButton;
    __weak NSTextFieldCell *_loadingText;
    __weak NSButton *_installlButton;
    __weak NSTextFieldCell *_errorText;
    __weak NSTextFieldCell *_installTargetPathText;
}

@property (assign) IBOutlet NSWindow *window;
- (IBAction)tapped:(id)sender;

@property (weak) IBOutlet NSButton *installlButton;
@property (weak) IBOutlet NSTextFieldCell *loadingText;
@property (weak) IBOutlet NSButton *greenButton;
@property (weak) IBOutlet NSProgressIndicator *InstallingIndicator;
@property (weak) IBOutlet NSButton *redButton;
@property (weak) IBOutlet NSTextFieldCell *errorText;
@property (weak) IBOutlet NSTextFieldCell *installTargetPathText;
@end
