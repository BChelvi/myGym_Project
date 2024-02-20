import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UserlistComponent } from './userlist/userlist.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,UserlistComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'myGym_FrontEnd';
}
