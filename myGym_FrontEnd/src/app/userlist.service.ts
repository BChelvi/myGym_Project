import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable,combineLatest,map,switchMap, catchError, throwError,tap,of, shareReplay } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserlistService {

  constructor(private http: HttpClient) { }

  getUsers(): Observable<any[]> {
    return this.http.get<any[]>('http://localhost:8000/users/');
  }


}
