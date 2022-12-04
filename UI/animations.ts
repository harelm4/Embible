import {
  animate,
  state,
  style,
  transition,
  trigger,
} from '@angular/animations';

export const fadeIn = trigger('fadeIn', [
  transition(':enter', [
    style({
      opacity: 0,
    }),
    animate('{{time}}'),
    style({ opacity: 1 }),
  ]),
]);

export const fadeOut = trigger('fadeOut', [
  transition(':leave', [animate('{{time}} ease-out'), style({ opacity: 0 })]),
]);

export const fadeInOut = trigger('fadeIn', [
  state('open', style({ opacity: 1 })),
  state('closed', style({ opacity: 0 })),
  transition('open => closed', animate('1s ease-out')),
  transition('closed => open', animate('1s ease-in')),
]);
