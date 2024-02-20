import { Component } from '@angular/core';
import { UserlistService } from '../userlist.service';

@Component({
  selector: 'app-userlist',
  standalone: true,
  imports: [],
  templateUrl: './userlist.component.html',
  styleUrl: './userlist.component.css'
})
export class UserlistComponent {

  users : any[] =[];

  constructor(private userlistService: UserlistService) { }

  ngOnInit() {
    this.userlistService.getUsers().subscribe(
      users => {
        // Faites quelque chose avec les données récupérées, par exemple les stocker dans une variable
        this.users = users;
      },
      error => {
        // Gérez les erreurs en cas de problème avec la requête HTTP
        console.error('Une erreur s\'est produite :', error);
      }
    );
  }

}
